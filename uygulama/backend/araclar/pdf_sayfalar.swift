// PDF'in her sayfasını PNG'ye çevirir (macOS PDFKit). Kullanım: swift pdf_sayfalar.swift girdi.pdf cikti_klasoru [olcek]
import PDFKit
import AppKit
let args = CommandLine.arguments
guard args.count >= 3, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else { print("PDF açılamadı"); exit(1) }
let scale: CGFloat = args.count > 3 ? CGFloat(Double(args[3]) ?? 2.0) : 2.0
print("sayfa:", doc.pageCount)
for i in 0..<doc.pageCount {
    let page = doc.page(at: i)!
    let r = page.bounds(for: .mediaBox)
    let img = NSImage(size: NSSize(width: r.width * scale, height: r.height * scale))
    img.lockFocus()
    NSColor.white.set(); NSRect(x: 0, y: 0, width: r.width * scale, height: r.height * scale).fill()
    let ctx = NSGraphicsContext.current!.cgContext
    ctx.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx)
    img.unlockFocus()
    let png = NSBitmapImageRep(data: img.tiffRepresentation!)!.representation(using: .png, properties: [:])!
    try! png.write(to: URL(fileURLWithPath: "\(args[2])/sayfa\(i + 1).png"))
}
